var addTwoNumber = function ( l1, l2) {
    let res = new ListNode(null);
    let last = res;
    let carry = 0;
    while ( l1 || l2){
        last.next = new ListNode(null);
        last = last.next;
        let left = l1 ? l1.val : 0;
        let right = l2 ? l2.val : 0;
        let total = left + right + carry;
        if( total > 10){
            carry = 1;
            last.val = total - 10;
        }
        else {
            carry = 0;
            last.val = total;
        }
        l1 = l1 ? l1.next : null;
        l2 = l2 ? l2.next : null;
    }
    if (carry==1){
        last.next = new ListNode(1)
    }
    return res.next;
}
for(let i=0;i<as.length;i++){
    
}