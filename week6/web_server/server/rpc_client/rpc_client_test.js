var client=require('./rpc_client')

client.add(1,2,function (resposne){
    console.assert(resposne==3);
})