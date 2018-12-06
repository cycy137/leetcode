var mergeTwoLists = function (l1, l2) {
    let res = new Nodelist(null);
    let tmp = res;
    while (l1 && l2){
        if(l1.val < l2.val){
            tmp.next = l1;
            l1 = l1.next;
        }
        else{
            tmp.next = l2;
            l2 = l2.next;
        }
        tmp = tmp.next;
    }
    if (l1){
        tmp.next = l1;
    }
    if(l2){
        tmp.next = l2;
    }
    return res.next;
    // let fir = new NodeList(null);
    // let res = fir;
    // while (l1 && l2){
    //     if( l1.val < l2.val){
    //         res.next = l1;
    //         l1 = l1.next;
    //     }
    //     else{
    //         res.next = l2;
    //         l2 = l2.next;
    //     }
    //     res = res.next;
    // }
    // if (l1){
    //     res.next = l1;
    // }
    // if(l2){
    //     res.next = l2;
    // }
    // return fir.next;
}