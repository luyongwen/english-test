function change() {
    // var t = document.getElementById('en_ch');
    // var elements = document.getElementById('ch');
    var elements = document.getElementsByClassName('pure-table-odd');
    ma = elements.length;
    for (var i =0; i < ma; i++) {
        element = elements[i];
        // console.log(elements[i]);
        if (element.style.visibility == 'hidden') {
            element.style.visibility = 'visible';// 以块级元素显示
        } else {
            element.style.visibility = 'hidden'; // 隐藏
        }
    }
    // for (var element in elements) {
    //     if (element.style.visibility == 'hidden') {
    //         element.style.visibility = 'visible';// 以块级元素显示
    //     } else {
    //         element.style.visibility = 'hidden'; // 隐藏
    //     }
    // }
    // for (var element in elements) {
    //     console.log(element)
    // }
    // console.log(elements[0]);
}