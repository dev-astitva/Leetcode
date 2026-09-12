class Solution {
    public int[] maxSlidingWindow(int[] nums,int k){
    if(nums==null||k<=0){
        return new int[0];
    }

    int size=nums.length;
    int[] res=new int[size-k+1];
    int index=0;
    Deque<Integer> deque=new ArrayDeque<>();

    for(int curr=0;curr<size;curr++){
        while(!deque.isEmpty()&&deque.peekFirst()<curr-k+1){
            deque.pollFirst();
        }

        while(!deque.isEmpty()&&nums[deque.peekLast()]<nums[curr]){
            deque.pollLast();
        }

        deque.addLast(curr);

        if(curr>=k-1){
            res[index]=nums[deque.peekFirst()];
            index++;
        }
    }

    return res;
    }
}