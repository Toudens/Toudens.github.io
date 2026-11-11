// Keep short Chinese sentence endings together at every viewport width.
// Touch only ordinary text; formulas and inline formatting remain intact.
document.querySelectorAll('.content p').forEach((paragraph) => {
  const walker = document.createTreeWalker(paragraph, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      return node.parentElement.closest('mjx-container, script, style')
        ? NodeFilter.FILTER_REJECT
        : NodeFilter.FILTER_ACCEPT;
    },
  });
  let lastText;
  while (walker.nextNode()) {
    if (walker.currentNode.data.trim()) lastText = walker.currentNode;
  }
  if (!lastText) return;

  const ending = lastText.data.match(/([\p{Script=Han}]{4,6}[。，；：！？][”’」』）]?)(\s*)$/u);
  if (ending) {
    const tail = lastText.splitText(ending.index);
    tail.splitText(ending[1].length);
    const span = document.createElement('span');
    span.className = 'ddpm-sentence-end';
    tail.replaceWith(span);
    span.append(tail);
  } else if (/[\p{Script=Han}][。，；：！？][”’」』）]?\s*$/u.test(lastText.data)) {
    // A formula or emphasis can leave too little plain text to group.
    paragraph.classList.add('ddpm-balance-end');
  }
});
