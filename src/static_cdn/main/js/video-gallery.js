let listVideo = document.querySelectorAll('.video-list .vid')
let mainVideo = document.querySelector('.main-video video')
let title = document.querySelector('.title-vid')

$(document).ready(function() {
  $('.video-list div:first').addClass('active');
});

listVideo.forEach(video =>{
    video.onclick = () => {
        listVideo.forEach(vid => vid.classList.remove('active'));
        video.classList.add('active');
        if(video.classList.contains('active')){
            let src = video.children[0].getAttribute('src');
            mainVideo.src = src;
            let text = video.children[1].innerHTML;
            title.innerHTML = text;
        };
    };
});