---
title: 偷一偷QwQ
comments: false
weight: "4"
---
\
{{< travel-map >}}
[
  {"name": "西安", "value": 1},
  {"name": "温州", "value": 1},
  {"name": "金华", "value": 1},
  {"name": "丽水", "value": 1},
  {"name": "上海", "value": 1},
  {"name": "衢州", "value": 1},
  {"name": "舟山", "value": 1},
  {"name": "绍兴", "value": 1},
  {"name": "宁波", "value": 1},
  {"name": "南京", "value": 1},
  {"name": "青岛", "value": 1},
  {"name": "大连", "value": 1},
  {"name": "北京", "value": 1},
  { "name": "武汉", "value": 2,  "url": "/ttneed/wuhan/"},
  { "name": "杭州", "value": 2, "url": "/ttneed/hangzhou/" },
  { "name": "渭南", "value": 2, "url": "/ttneed/weinan/" }
]
{{< /travel-map >}}

<style>
  @import url('https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap');

  .polaroid-gallery {
    margin-top: 2rem;
    padding: 1rem;
    max-width: 1100px;
    margin-left: auto !important;
    margin-right: auto !important;
  }

  .polaroid-gallery > div {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important; 
    gap: 2.5rem 1.5rem !important;
  }

  /* --- 基础卡片样式 --- */
  .art-card {
    background-color: #ffffff !important; /* 浅色背景 */
    padding: 10px 10px 42px 10px !important; 
    border-radius: 2px !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
    min-height: auto !important; 
    aspect-ratio: 4 / 4.9 !important; 
    display: flex !important;
    flex-direction: column !important;
    overflow: visible !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    border: 1px solid #f0f0f0 !important;
  }

  /* --- 深色模式卡片适配 --- */
  .dark .art-card {
    background-color: #1a1a1a !important; /* 深灰色背景 */
    border-color: #333333 !important;     /* 暗色边框 */
    box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important; /* 更重的阴影 */
  }

  /* --- 背景图样式 --- */
  .custom-bg-full {
    position: relative !important;
    width: 100% !important;
    height: 86% !important; 
    object-fit: cover !important;
    filter: brightness(0.95) contrast(90%);
    transition: all 0.4s ease;
    display: block !important;
    border: 1px solid #f0f0f0; 
  }

  /* 深色模式下的图片边框 */
  .dark .custom-bg-full {
    border-color: #262626 !important;
  }

  /* --- 标题文字样式 --- */
  .art-card span, 
  .art-card h3, 
  .art-card div[class*="title"],
  .art-card .hextra-feature-card-title {
    display: block !important;
    position: absolute !important;
    bottom: 6px !important; 
    left: 0 !important;
    width: 100% !important;
    text-align: center !important;
    font-family: 'Zhi Mang Xing', serif !important;
    font-size: 1.8rem !important; 
    color: #222 !important; /* 浅色模式深色字 */
    margin: 0 !important;
    padding: 0 !important;
    z-index: 10 !important;
    font-weight: normal !important;
    transition: color 0.4s ease;
  }

  /* 深色模式下的文字颜色 */
  .dark .art-card span, 
  .dark .art-card h3, 
  .dark .art-card div[class*="title"] {
    color: #eeeeee !important; /* 深色模式浅色字 */
  }

  /* --- 交互与布局 --- */
  .polaroid-gallery > div > :nth-child(3n+1) { transform: rotate(-2deg); }
  .polaroid-gallery > div > :nth-child(3n+2) { transform: rotate(1.5deg) translateY(-8px); }
  .polaroid-gallery > div > :nth-child(3n+3) { transform: rotate(-1deg) translateY(5px); }

  .art-card:hover {
    transform: rotate(0deg) scale(1.06) translateY(-10px) !important;
    z-index: 100 !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15) !important;
  }

  /* 深色模式悬停阴影加强 */
  .dark .art-card:hover {
    box-shadow: 0 25px 50px rgba(0,0,0,0.6) !important;
  }

  .art-card:hover .custom-bg-full {
    filter: brightness(1) contrast(100%);
  }

  .art-card svg { display: none !important; }

  @media (max-width: 768px) {
    .polaroid-gallery > div { grid-template-columns: 1fr 1fr !important; }
  }
</style>

<div class="polaroid-gallery">
{{< cards >}}
  {{< hextra/feature-card
    title="繁花"
    link="/ttneed/flower"
    image="https://toudens-images.s3.bitiful.net/flower/01.jpg?no-wait=on&w=1200&q=80&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="流云"
    link="/ttneed/cloud"
    image="https://toudens-images.s3.bitiful.net/cloud/04.jpg?w=1200&q=80&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="渭南"
    link="/ttneed/weinan"
    image="https://toudens-images.s3.bitiful.net/huashan/01.jpg?w=1200&q=80&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="武汉"
    link="/ttneed/wuhan"
    image="https://toudens-images.s3.bitiful.net/wuhan/02.jpg?w=1200&q=80&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="杭州"
    link="/ttneed/hangzhou"
    image="https://toudens-images.s3.bitiful.net/liangzhu/DSC00622.jpg?w=1200&q=80&fmt=webp" 
    class="art-card"
    imageClass="custom-bg-full"
  >}}
{{< /cards >}}
</div>