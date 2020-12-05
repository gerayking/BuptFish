$(function(){
	//单选点击
	var falg = true;
	$(".dark-check").click(function(){
		$(this).toggleClass('action');
		if(falg){
			cart(1);
		}else{
			cart(1);
		}
	})
	//删除
	$("#del").click(function(){
		$(".list ul li").each(function(item,ind){
			if($(this).find('.dark-check').hasClass('action')){
				$(this).remove();
			}
		})
	})
	
	$(".add").click(function(){
		var num = parseInt($(this).siblings('.num').val());
		var price = parseInt($(this).parents('.m-num').siblings('.price').find('span').data('price'));
		var sum = parseInt(num+1);
		$(this).siblings('.num').val(sum);
		var all = parseInt(sum *price);
		$(this).parents('.m-num').siblings('.price').find('span').text(all)
		
	})
	$(".jian").click(function(){
		var num = parseInt($(this).siblings('.num').val());
		var price = parseInt($(this).parents('.m-num').siblings('.price').find('span').data('price'));
		if(num >1){
			var sum = parseInt(num-1);
			$(this).siblings('.num').val(sum);
			console.log(sum)
			var all = parseInt(sum *price);
			$(this).parents('.m-num').siblings('.price').find('span').text(all)
		}else{
			alert('购买件数不能小于1')
		}
	})
	
	//全选点击
	$(".gap-check").click(function(){
		if(falg){
			cart(2);
		}else{
			cart(2);
		}
		
	})
})
//公用方法
function cart(id){
	//选择总长度
	var Alldark = $(".dark-check").length;
	//已选择长度
	var dark = $(".dark-check.action").length;
	console.log(dark)
	//其实全选和单选都一样 2是全选 1是单选
	if(id==2||id==1){
		if(Alldark!=dark&&id==2){ //判断是否全选
			$(".dark-check,.gap-check").addClass('action');
			$("#del").show();
		}else if(Alldark==dark&&id==2){ //全选了后去掉全选
			$(".dark-check,.gap-check").removeClass('action');
			$("#del").hide();
		}else if(dark==0&&id==1){//判断单选没有一个选中
			$("#del").hide();
		}else if(Alldark==dark&&id==1){//如果单选按钮全亮就点亮全选按钮
			$("#del").show();
			$(".gap-check").addClass('action');
		}else if(Alldark!=dark&&id==1){//如果单选按钮未全亮就取消全选按钮的点亮
			$("#del").show();
			$(".gap-check").removeClass('action');
		}
		//获取list中的价格
		var list = [];
		$(".list ul li").each(function(item,ind){
			if($(this).find('.dark-check').hasClass('action')){
				list.push($(this).find('.price span').text());
			}
		})
		//总价
		var arr = list.length;
		var sum=0;
		for(var i=0; i<arr; i++){
			var num =parseInt(list[i]);//要先把价格变为int类型
			sum =parseInt(num+sum);
		}
		if(sum==0){
			sum= '0.00';
		}
		$(".all-price span").text(sum);
	}
}