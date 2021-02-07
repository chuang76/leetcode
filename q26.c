#include <stdio.h>
#include <stdlib.h>

int removeDuplicates(int* nums, int numsSize)
{
	if (numsSize == 0)
		return 0; 

    int unique = 0; 		// started from 0 
    // 1, 1, 2
    // 0, 1, 2
    // unique = 0, i = 1, same -> continue
    // unique = 0, i = 2, diff -> unique = 1, nums[1] = nums[2]; 

    for (int i = 1; i < numsSize; i++) {
    	if (nums[i] != nums[unique]) {
    		unique++;                         // update unique 
    		nums[unique] = nums[i]; 
    	}
    }
    
    return unique + 1; 
}

int main(int argc, char** argv)
{
	// int nums[] = {1, 1, 2}; 
	int nums[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4}; 
	int ret = removeDuplicates(nums, sizeof(nums) / sizeof(nums[0])); 

	for (int i = 0; i < ret; i++)
		printf("nums[%d] = %d\n", i, nums[i]); 

	return 0; 
}