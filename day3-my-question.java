class Solution {
  public int singleNonDuplicate(int[] nums) {
    int n = nums.length;
    int k =0;
    if(n == 1){
      return 1;
    }
    int j = 1;
    for(int i = 0; i < n ;){
      if(nums[i] == nums[j]){
        i+=2;
        if(i == n-1 && j == n-2){
            k = nums[i];
            return k;
            }   
      else{
        j+=2;
        }
    }
    else{
        k = nums[i];
        break;
    }
}
return k;
}
}
