function getmovie(){
    fetch('/recommend')
    .then(response => response.json())
    .then(data=>{
        document.getElementById("movieTitle").innerText = data.title;
        document.getElementById("movieImage").src = `static${data.image}`;
        
    })
}
function book(title){
     alert("you booked this movie ${title}")
}
function details(title){
     alert("This movie name $(title) /n Category:comedy /n has 5 rating")
}
function fav(title){
    alert("you added ${title} to your favorites")
}
function trailer(title){
     alert("please wait $(title) trailer is loading...")
}