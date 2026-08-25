---
title: 偷一偷在南昌
weight: "7"
---

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
  /* 已移除倾斜（rotate）效果，所有卡片保持水平 */

  .art-card:hover {
    transform: scale(1.05) translateY(-10px) !important;
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
    title="江西省美术馆"
    link="/ttneed/nanchang/art-museum"
    image="https://toudens-images.s3.bitiful.net/nanchang/art/0.jpg?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="滕王阁"
    link="/ttneed/nanchang/tengwang"
    image="https://toudens-images.s3.bitiful.net/nanchang/tengwang/2.jpg?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="南昌舰163"
    link="/ttneed/nanchang/nanchang163"
    image="https://toudens-images.s3.bitiful.net/nanchang/nanchang163/DSC01003.JPG?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="江西小炒"
    link="/ttneed/nanchang/delicacies"
    image="https://toudens-images.s3.bitiful.net/nanchang/food/0.jpg?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="南昌海洋馆"
    link="/ttneed/nanchang/ocean-park"
    image="https://toudens-images.s3.bitiful.net/nanchang/ocean/DSC01110.JPG?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="海昏侯国遗址"
    link="/ttneed/nanchang/haihun"
    image="https://toudens-images.s3.bitiful.net/nanchang/haihun/DSC01253.JPG?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="江西省博物馆"
    link="/ttneed/nanchang/jx-museum"
    image="https://toudens-images.s3.bitiful.net/nanchang/jx-museum/DSC01342.JPG?w=1600&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="八一馆"
    link="/ttneed/nanchang/81"
    image="https://toudens-images.s3.bitiful.net/nanchang/81/DSC01385.JPG?w=1600&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="南昌散景"
    link="/ttneed/nanchang/other"
    image="https://toudens-images.s3.bitiful.net/nanchang/other/1.jpg?w=1200&q=100&fmt=webp"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
{{< /cards >}}
</div>