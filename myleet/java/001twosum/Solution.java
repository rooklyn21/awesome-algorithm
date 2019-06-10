import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> lookup = new HashMap<>();
        int[] res = new int[2];
        for (int i = 0; i < nums.length; i++) {
            if (lookup.containsKey(target - nums[i])) {
                res = new int[] { lookup.get(target - nums[i]), i };
                break;
            } else {
                lookup.put(nums[i], i);
            }
        }
        return res;
    }
    public static void main(String args[]){
        int[] list1 = {2, 7, 11, 15};
        Solution sl =new Solution();
        int[] list2 = sl.twoSum(list1,9);
        for(int i:sl.twoSum(list1,9)){
            System.out.println(i);
        }
        // System.out.println(sl.twoSum(list1,9));
    }
}




