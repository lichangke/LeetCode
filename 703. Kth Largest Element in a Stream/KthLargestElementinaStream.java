/*
 *@author:leacoder
 *@des:  优先队列 数据流中的第K大元素
 */

class KthLargest {
    final PriorityQueue<Integer> myqueue;
    final int kMax;

    public KthLargest(int k, int[] nums) {
        myqueue = new PriorityQueue<>(k);  //指定初始容量k的优先队列
        kMax = k;
        for(int n:nums){
            add(n); //将数据加入到 优先队列中
        }
    }
    
    public int add(int val) {
        if(myqueue.size()<kMax){
            myqueue.offer(val); //队列还未填满 直接入队
        }
        else if(myqueue.peek()<val){//队列顶 小于加入的val 说明第k大变为val，原来的变为k+1大
            myqueue.poll();
            myqueue.offer(val);  //移除顶端 数据 加入新数据
        }
        
        return myqueue.peek(); 
            
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */