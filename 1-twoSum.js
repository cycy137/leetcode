var twoSum = function (nums, targets) {
    let res = {};
    for (let i = 0; i < nums.length; i++){
        if ( i == undefined){
            res[targets-nums[i]] = i;
        }
        else {
            return [res[nums[i]],i];
        }
    }
}