class Solution {
    public int[] twoSum(int[] nums, int target) {
        int ans;
        int[] index = new int[2];;
        for(int i=0; i<nums.length;i++){
            ans = nums[i];
            for(int j=i+1; j<nums.length; j++){
                ans = ans + nums[j];
                if(ans==target){
                    index[0] =  i;
                    index[1] = j;
                    break;
                }
                ans = nums[i];
            }
            if(ans==target){
                ans = 0;
                i = 0;
                break;
            }
        }
        
        return index;
    }
}