// 组装一个JSON数组
var postModel = [];
postModel.push({a:1,b:2});
postModel.push({c:3,d:4});

// 发送的是一个对象，对象的值先转换为字符串
$.post('url...', {works: JSON.stringify(postModel)}, function (data) {
        alert('ok');
});