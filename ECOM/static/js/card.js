var updateBtns = document.getElementsByClassName('update-card')

for(var i=0; i<updateBtns.length; i++){
	updateBtns[i].addEventListener('click',function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:',productId,'action:',action);
		console.log('User:',user);

		if(user === 'AnonymousUser'){
			console.log('Bu user saytga kirmagan')
		}
		else{
			updateUserOrder(productId,action);

		}

		}
	)
}

function updateUserOrder(productId,action){
	console.log('User saytga kirdi,datani yuboring..')
}
