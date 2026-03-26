---
title: "计算机科学"
---
<!-- 直接把卡片放在这个 div 里，不要再用 feature-grid -->
<div style="display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(max(280px, calc(50% - 16px)), 1fr)); margin-top: 1.5rem;">

  {{< hextra/feature-card 
    title="数字逻辑设计" 
    link="/compsci/dd" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="数据库系统" 
    link="/compsci/db" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="计算机体系结构" 
    link="/compsci/ca" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="离散数学" 
    link="/compsci/dm" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}
  
{{< hextra/feature-card 
    title="面向对象程序设计" 
    link="/compsci/oop" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}
  <!-- 在这里继续补充你剩下的其他课程卡片 -->

</div>