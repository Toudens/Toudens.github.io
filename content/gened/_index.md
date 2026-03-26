---
title: 通识课
---
<!-- 直接把卡片放在这个 div 里，不要再用 feature-grid -->
<div style="display: grid; gap: 16px; grid-template-columns: repeat(auto-fit, minmax(max(280px, calc(50% - 16px)), 1fr)); margin-top: 1.5rem;">

  {{< hextra/feature-card 
    title="军事理论" 
    link="/gened/militheory" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="马克思主义基本原理" 
    link="/gened/marxism" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="思想道德与法治" 
    link="/gened/morality" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}

  {{< hextra/feature-card 
    title="心理卫生" 
    link="/gened/menhealth" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}
  
{{< hextra/feature-card 
    title="经济法理论与实务" 
    link="/gened/ecolaw" 
    class="aspect-auto md:aspect-[1.8/1] max-md:min-h-[250px]" 
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,0,0,0),hsla(0,0%,100%,0));" 
  >}}
  <!-- 在这里继续补充你剩下的其他课程卡片 -->

</div>