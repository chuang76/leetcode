#include <stdio.h>
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize)
{
    int i, j;
    returnSize = 2;               
    int *arr; 
    arr = (int *) malloc(sizeof(int) * 2); 
    
    for (i = 0; i < numsSize; i++)
    {
        for (j = i + 1; j < numsSize; j++)
        {
            if ((nums[i] + nums[j]) == target)
            {
                arr[0] = i;
                arr[1] = j;
                return arr;
            }
        }
    }
    return arr;
}

int main(int argc, char** argv)
{
    int nums[] = {2, 7, 11, 15};
    int numsSize = 4; 
    int target = 9; 
    int* returnSize; 
    int* result = twoSum(nums, numsSize, target, returnSize); 
    printf("Output = [%d, %d]\n", result[0], result[1]);

    return 0; 
}