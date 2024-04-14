/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    if (x < 0) {
        return false;
    }
    let reversed = 0;
    let temp = x;

    while(temp!==0){
        const num = temp%10;
        reversed = reversed * 10 + num;
        temp = Math.floor(temp/10);
    }
    return reversed === x
};