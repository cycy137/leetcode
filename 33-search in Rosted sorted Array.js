var search = function(nums, target) {
    let first = 0;
    let finall = nums.length-1;
    while(finall>= first){
        let mid = Math.floor((first+finall)/2);
        // left + Math.floor((right - left) / 2)
        if (nums[mid]===target){
            return mid;
        }
        if(nums[first] <= nums[mid]){
            if(nums[first] < target && target < nums[mid]){
                finall = mid;
            }
            else{
                first = mid;
            }
        }
        else{
            if( nums[mid]<target && target < nums[finall]){
                first = mid;
            }
            else{
                finall = mid;
            }

        }
        console.log(mid)
    }
    return -1;
};
