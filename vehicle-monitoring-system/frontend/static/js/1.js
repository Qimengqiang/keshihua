// 开发调试用 ↓↓↓
window.addEventListener('error', function(e) {
    alert(`JS错误: ${e.message}\n在 ${e.filename} 第 ${e.lineno} 行`);
});
// 检查绘图管理器是否加载
console.log('DrawingManager状态:', typeof drawingManager !== 'undefined' ? '已加载' : '未加载')
// 检查接口可用性
fetch('/parking-areas/').then(r => console.log('接口响应:', r.status))