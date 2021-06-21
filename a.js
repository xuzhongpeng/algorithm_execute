
function b(callback){
  callback()
}

function c(){
  let d = '1'
  function a(){
    console.log(d)
  }
  b(a)
}