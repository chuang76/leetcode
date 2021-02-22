// find unique 

#include <stdio.h>
#include <stdlib.h>

int singleNumber(int* nums, int numsSize)
{
    int ans = 0; 
    for (int i = 0; i < numsSize; i++) {
        ans ^= nums[i]; 
    }
    return ans; 
}

int main(int argc, char** argv)
{
    int nums[] = {2, 2, 1};
    int ans = singleNumber(nums, sizeof(nums) / sizeof(nums[0])); 
    printf("ans = %d\n", ans); 
    return 0; 
}