var addBinay = function (a, b) {
    if (a.length > b.length){
        return addBinay(b, a);
    }
    let arr = [];
    let carry = "0";
    for( let i = 0; i < b.length; i++){
        let charA = i < a.length ? a.charAt( a.length - 1 - i) ? "0";
        let charB = b.charAt( b.length -1-i );
        let current;
        if( charA != charB){
            current = carry == "1" ? "0" : "1";
        }
        else{
            current = carry;
            carry = charA;
        }
        arr.unshift(current);

    }
    if( carry == "1"){
        arr.unshift(carry);
    }
    return arr.join("");
}