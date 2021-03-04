class Solution {
    fun solution(s: String): Boolean {
        var answer = true
        // var a : Char
        // val li = listOf("0","1","2","3","4","5","6","7","8","9")
        if ((4==s.length) or (s.length==6)){
            for(i in s){
                // a=i.toChar()
                if (i !in '0'..'9'){
                    return false
                }
            }
        }
        else{
            return false
        }
        return answer
    }
}
