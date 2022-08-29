var updateBtns = document.getElementsByClassName('update-cart');

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var courseId = this.dataset.course
        var action = this.dataset.action

        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(courseId, action)
        }

    })
}

function updateUserOrder(courseId, action){
    console.log('logged in and sending data ...')
    var url = '/order/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'courseId': courseId, 'action': action})
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data', data)
            location.reload()
            })
}