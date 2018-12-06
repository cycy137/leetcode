var canJump = function(nums) {
    let max = 0;
    for(let i=nums.length-1;i>=0; i--){
        if(nums[i]+i >= max){
            max= i;
        }
    }

    return max ==0;
