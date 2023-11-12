# My-Blockchain

嘗試實作blockchain，目前不支持尋找其他節點功能

程式碼分三個部分：
```
BlockchainNode
├─ Blockchain
└─ BlockMiner
```

## BlockchainNode
節點

運行後可以由
1. `localhost:port/get_chain`獲得當前鏈的所有資料
2. `localhost:port/get_state`查看鏈的一些統計數據，以及鏈的正確性

![](/get_chain_demo.png)
![](/get_state_demo.png)

## Blockchain
目前PoW的難度固定在5，算法採用leading zero

## BlockMiner
礦工程序，支持異步挖礦


# Build
```
pip install -r requirements.txt
```

# Run
```
python main.py
```
