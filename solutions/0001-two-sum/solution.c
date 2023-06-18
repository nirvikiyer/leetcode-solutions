/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int outsideIndex = 0;
    int insideIndex = 1;
    int found = 0;

    for (; outsideIndex < numsSize; outsideIndex++) {
        for (insideIndex = outsideIndex+1; insideIndex < numsSize; insideIndex++) {
            if (target == nums[outsideIndex] + nums[insideIndex]) {
                found = 1;
                break;
            }
        }
        if (found) break;
    }
    if (found) {
        int *ret = (int *)malloc (2*sizeof(int));
        ret[0] = outsideIndex;
        ret[1] = insideIndex;

        printf ("Found: %d %d %d and %d\n", ret[0], ret[1],outsideIndex, insideIndex);

        *returnSize = 2;
        return ret;
    }
    *returnSize = 0;
    return NULL;
}
