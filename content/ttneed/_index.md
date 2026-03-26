---
title: "偷一偷QwQ"
---
<style>
  /* 引入谷歌免费开源中文字体：只莽行书 */
  @import url('https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap');

  /* 1. 外层无缝画廊大画框 */
  .seamless-gallery {
    border-radius: 16px;       
    overflow: hidden;          
    box-shadow: 0 10px 30px rgba(0,0,0,0.15); 
    margin-top: 1.5rem;
    background-color: #000;    
  }

  /* 2. 强制抹除 Hextra 默认的属性 */
  .seamless-gallery > div {
    gap: 0 !important;
    margin-top: 0 !important; /* 【核心修复1】抹除 Hextra 自带的顶部外边距，消灭顶端黑框 */
    padding: 0 !important;
  }

  /* 3. 卡片本身：削平圆角，去除边框，严丝合缝 */
  .art-card {
    border-radius: 0 !important; 
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
    
    /* 【核心修复2】统一在这里增加高度！400px 觉得不够可以改成 450px 或 500px */
    min-height: 180px !important; 
    
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    overflow: hidden !important;
    position: relative !important; /* 确保背景图只在卡片内部绝对定位 */
  }

  /* 4. 背景图铺满 */
  .custom-bg-full {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    width: 100% !important;
    height: 100% !important;
    object-fit: cover !important;
    filter: brightness(0.7);
    z-index: 0;
    pointer-events: none;
    transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1);
  }

  .art-card:hover .custom-bg-full {
    transform: scale(1.08);
  }

  /* 5. 艺术字 */
  .art-card div[class*="font-bold"], 
  .art-card h3 {
    position: relative;
    z-index: 10;
    font-size: 4rem !important; /* 图片变高了，字也可以稍微调大一点点 */
    line-height: 1 !important;
    font-weight: normal !important;
    font-family: 'Zhi Mang Xing', 'Xingkai SC', 'STXingkai', '华文行楷', 'KaiTi', serif !important;
    color: #ffffff !important;
    text-shadow: 
      0px 3px 8px rgba(0, 0, 0, 0.9),
      0px 0px 25px rgba(0, 0, 0, 0.6);
    margin: 0 !important;
  }

  .art-card svg {
    display: none !important;
  }
</style>

<!-- html 结构部分 -->
<div class="seamless-gallery">
{{< cards >}}
  {{< hextra/feature-card
    title="花"
    link="/ttneed/flower"
    image="/images/flower.jpg"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
  {{< hextra/feature-card
    title="云"
    link="/ttneed/cloud"
    image="/images/cloud.jpg"
    class="art-card"
    imageClass="custom-bg-full"
  >}}
{{< /cards >}}
</div>