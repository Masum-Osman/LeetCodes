    for(var i = 0; i < nums.length; i++)
        {
            for(var j = i+1; j < nums.lenght - i; j++)
                {
                    if(nums[i] + nums[j] == target)
                        {
                            // result.push(i);
                            // result.push(j);
                            return i, j;
                        }
                }
        }
    // return result;