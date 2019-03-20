/*
@author:leacoder
@des:  优先队列 滑动窗口最大值
PriorityQueue 默认是一个小顶堆
*/
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if(k==0){
            return nums;
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>(k, (a, b) -> {return b-a;});//优先队列
        for (int i = 0; i < k; i++) {
            queue.add(nums[i]);
        }
        int[] res = new int[nums.length - k + 1];//存放结果
        
        for (int i = 0; i < res.length; i++) {
            res[i] = queue.peek(); //从取优先队列取出最大
            queue.remove(nums[i]);//删除 优先队列中nums[i]
            if (i + k < nums.length) {
                queue.add(nums[i + k]); //将新进入数 加入优先队列中
            }
        }
        
        return res;
    }
}

/*
PriorityQueue 默认是一个小顶堆，如何实现大顶堆
1、

PriorityQueue<Integer> pq = new PriorityQueue<>(n,(Integer a,Integer b)->{return b-a;});


2、
PriorityQueue<Integer> pq = new PriorityQueue<>(n, new Comparator<Integer>() {
    @Override
    public int compare(Integer integer, Integer t1) {
        return t1-integer;
    }
});

*/