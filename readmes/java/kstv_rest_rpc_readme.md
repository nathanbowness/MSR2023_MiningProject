# [english wiki](https://github.com/topcpporg/rest_rpc/wiki/English)
在此特别感谢社区的朋友刘丹将rest_rpc的中文说明翻译为英文。

#[chinese wiki](https://github.com/topcpporg/rest_rpc/wiki/Chinese)

##Contributer

[江南（qicosmos）](https://github.com/qicosmos)，[IndignantAngel](https://github.com/IndignantAngel)

##Contact us
qicosmos@163.com

--------------------------

## rest_rpc v0.91 release note
#### 新增特性
1.业务函数的参数可以有connection_ptr，也可以没有，取决于你的需要，使用更灵活。
```cpp
server.register_handler("add_with_conn", []
    (timax::rpc::connection_ptr conn, int a, int b)
{
    auto result = a + b;
    if (result < 1)
        conn->close();
    return result;
});
```
2.客户端添加private接口，拥有更高的权限和更多的流程控制

3.server端的pub提供了一个纯转发的重载实现

4.提供管理多个endpoint的工具
```cpp
auto endpoints = timax::rpc::get_tcp_endpoints("127.0.0.1:5001|127.0.0.1:5002");
for(auto const& endpoint : endpoints)
{
    std::cout << endpoint << std::endl;
}
```
5.客户端pub接口的，将会把转发协议的name当做topic，广播给所有监听这个topic的客户端，而不需要再服务器上注册handler；

6.服务器注册handler，将使用hash值代替字符串

#### Bug修复
1. rpc超时后异步调用链断开
2. 客户端和服务器read大块消息时，因使用boost::bind，而发生了意外地拷贝，招致读取到不正确的地址
3. 支持更低版本的编译器
