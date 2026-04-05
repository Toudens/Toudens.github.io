---
title: "偷一偷的朋友们"
width: "full"
---

<style>
/* ===== 让页面主容器真正铺满，无右侧空白 ===== */
.hextra-page-container {
    max-width: 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
}
.hextra-main {
    max-width: 100% !important;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}

/* ===== 朋友卡片网格 ===== */
.friends-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin-top: 2rem;
    margin-bottom: 2rem;
    width: 100%;
}
@media (max-width: 1024px) { 
    .friends-grid { grid-template-columns: repeat(2, 1fr); } 
}
@media (max-width: 640px) { 
    .friends-grid { grid-template-columns: 1fr; } 
}

/* ===== 卡片容器 ===== */
.friend-card {
    display: flex;
    min-height: 80px;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px; 
    overflow: hidden;   
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
    text-decoration: none !important;
    transition: all 0.3s ease;
}
html[class~="dark"] .friend-card {
    background: #1e1e20;
    border-color: #3f3f46;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}
.friend-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
}
html[class~="dark"] .friend-card:hover { 
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4); 
}

/* ===== 左侧文字区域 ===== */
.friend-info {
    flex: 1;             
    display: flex;
    flex-direction: column;
    justify-content: center; 
    padding: 0.6rem 1rem;
    min-width: 0;            
}
.friend-name {
    font-size: 1.15rem;
    font-weight: 800;
    color: inherit;
    margin-bottom: 0.2rem;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.friend-desc {
    font-size: 0.9rem;
    color: #666;
    line-height: 1.4;
    display: -webkit-box;
    -webkit-line-clamp: 2; 
    -webkit-box-orient: vertical;
    overflow: hidden;
}
html[class~="dark"] .friend-desc { 
    color: #aaa; 
}

/* ===== 右侧图片区域（占比更大，无分割线） ===== */
.friend-avatar-wrapper {
    width: 120px;               /* 从 85px 增加到 120px，头像占比更大 */
    flex-shrink: 0;          
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 0;
    /* 去掉 border-left，删除分割竖线 */
}
/* 图片：不裁剪、不放缩，保持原始比例 */
.friend-avatar {
    width: 100%;
    height: auto;
    max-height: 100%;
    object-fit: contain;
    transition: transform 0.3s ease;
}
.friend-card:hover .friend-avatar { 
    transform: scale(1.02);
}

/* 移动端无特殊处理（已无分割线） */
</style>

<div class="friends-grid">
    <!-- 偷一偷 -->
    <a href="/ttneed" class="friend-card" target="_blank" rel="noopener noreferrer">
        <div class="friend-info">
            <div class="friend-name">偷一偷</div>
            <div class="friend-desc">偷学统治世界！</div>
        </div>
        <div class="friend-avatar-wrapper">
            <img src="/images/Tou.jpg" alt="偷一偷" class="friend-avatar">
        </div>
    </a>
    <!-- 舔一舔合众国（修正拼写错误） -->
    <a href="https://licking.life" class="friend-card" target="_blank" rel="noopener noreferrer">
        <div class="friend-info">
            <div class="friend-name">舔一舔合众国</div>
            <div class="friend-desc">睡觉是为了起床，起床是为了睡觉</div>
        </div>
        <div class="friend-avatar-wrapper">
            <img src="/headimg/Tui.jpg" alt="舔一舔" class="friend-avatar">
        </div>
    </a>
    <!-- 凑数测试 -->
</div>