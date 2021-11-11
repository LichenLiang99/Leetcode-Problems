class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        Map<Integer, Integer> mapp = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++){
            if(mapp.containsKey(target - nums[i])){
                res[1] = i;
                res[0] = mapp.get(target - nums[i]);
                return res;
            }
            else{
                mapp.put(nums[i], i);
            }
        } 
        return res;
    }
}