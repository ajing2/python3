/***
 * 扩展的方法
 */
jQuery.extend({
	go:function(url){
		window.location.href=url;
	},
	alert:function (msg) {
		swal({title:msg});
	},
	confirm:function(msg,callback){
		swal({
			title : msg,
			type : "warning",
			showCancelButton : true,
			confirmButtonColor : "#DD6B55",
			confirmButtonText : "确定",
			cancelButtonText : "取消",
			closeOnConfirm : false
		}, function(){
			callback.call(this);  
		});	
	},
	exportExcel:function(url){
		this.exportFile("确定要导出为EXCEL吗？",url,1);
		
	},exportCsv:function(url){
		alert(url);
		this.exportFile("确定要导出为CSV吗？",url,2);
		
	},exportFile:function(title,url,exportType){
		swal({
			title : title,
			type : "warning",
			showCancelButton : true,
			confirmButtonColor : "#DD6B55",
			confirmButtonText : "确定",
			cancelButtonText : "取消",
			closeOnConfirm : true
		}, function(){
			if(url.indexOf("?")!=-1){
				location.href = url+"&exportType="+exportType;
			}else{
				location.href = url+"?exportType="+exportType;
			}
		});	
		
	}
});
