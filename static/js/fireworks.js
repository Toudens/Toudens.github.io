(function () {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '999999';
    document.body.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    let particles =[];
    let animating = false;
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    function createParticles(x, y) {
        // 范围变大后，稍微增加几个粒子填补空白，看起来更饱满 (20 -> 25)
        const particleCount = 25; 
        
        for (let i = 0; i < particleCount; i++) {
            const hue = Math.floor(Math.random() * 40) + 200;
            const lightness = Math.floor(Math.random() * 40) + 40;
            const color = `hsl(${hue}, 100%, ${lightness}%)`;
            
            particles.push({
                x: x,
                y: y,
                angle: Math.random() * Math.PI * 2,
                // 【范围修改区 1：初始速度】
                // 原来是 * 6 + 2，现在提高到 * 10 + 4 (爆发力更强)
                speed: Math.random() * 6 + 4, 
                radius: Math.random() * 4 + 3, 
                color: color,
                alpha: 1,
                // 【范围修改区 2：存活时间】
                // 降低变透明的速度，让它们有足够的时间飞得更远
                decay: Math.random() * 0.014 + 0.01 
            });
        }
    }
    
    function updateParticles() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let active = false;
        
        for (let i = 0; i < particles.length; i++) {
            let p = particles[i];
            p.x += Math.cos(p.angle) * p.speed;
            p.y += Math.sin(p.angle) * p.speed + 1.2; 
            
            // 【范围修改区 3：空气阻力】
            // 原来是 0.94，现在改成 0.96，阻力变小，滑行距离变长
            p.speed *= 0.94; 
            
            p.alpha -= p.decay;
            
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.color.replace('hsl', 'hsla').replace(')', `, ${p.alpha})`);
            ctx.fill();
            
            if (p.alpha <= 0) {
                particles.splice(i, 1);
                i--;
            } else {
                active = true;
            }
        }
        
        if (active) {
            requestAnimationFrame(updateParticles);
        } else {
            animating = false;
        }
    }
    
    window.addEventListener('click', (e) => {
        createParticles(e.clientX, e.clientY);
        if (!animating) {
            animating = true;
            updateParticles();
        }
    });
})();