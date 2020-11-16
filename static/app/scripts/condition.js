$("#enc_child_1_1").chainedTo("#enc_parent_1");
$("#enc_child_1_2").chainedTo("#enc_parent_1,#enc_child_1_1");
$("#enc_parent_3").chainedTo("#enc_parent_1");
// $("#enc_day_field").chainedTo("#enc_parent_1");

$("#exc_child_1_1").chainedTo("#exc_parent_1");
$("#exc_child_1_2").chainedTo("#exc_parent_1,#exc_child_1_1");
$("#exc_parent_3").chainedTo("#exc_parent_1");

$("#trl_child_1_1").chainedTo("#trl_parent_1");
$("#trl_child_1_2").chainedTo("#trl_parent_1,#trl_child_1_1");
$("#trl_parent_3").chainedTo("#trl_parent_1");

$("#rsk_child_1_1").chainedTo("#rsk_parent_1");

$(function(){(
	$(".trial_cond").click(function(event) {
		var x = $(this).is(':checked');
		if (x === true) {
			$(this).parents(".checkbox-card").find(".pass-box").show();
		}
		else{
			$(this).parents(".checkbox-card").find('.pass-box').hide();
		}
	})
)});

$(document).ready(function(){
		$("#enc_parent_1").on('change', function(abc) {
			abc.preventDefault()
				if ( this.value === currentTime) { // For Only time
						$("#enc_div_time_field").show();
						$("#enc_div_day_field").hide().val('');
						$("#enc_div_child_1_1").hide().val('');
						$("#enc_child_1_2").hide().val('');
						$("#enc_div_parent_3").hide().val('');
				}
				else if (this.value === currentDay){ //For only Day
						$("#enc_div_day_field").show();
						$("#enc_div_time_field").hide().val('');
						$("#enc_div_child_1_1").hide().val('');
						$("#enc_div_child_1_2").hide().val('');
						$("#enc_div_parent_3").hide().val('');

				}
				else {
						$("#enc_div_time_field").hide().val(''); // For MA_Cross, ST, BB, MACD
						$("#enc_div_day_field").hide().val('');
						$("#enc_div_child_1_1").show();
						$("#enc_div_child_1_2").show();
						$("#enc_div_parent_3").show();
				}
				if (this.value === 'pattern')   { // For Pattern
					$("#enc_div_child_1_2").hide().val('');
				}
		});
});

$(document).ready(function(){
		$("#exc_parent_1").on('change', function(abc) {
			abc.preventDefault()
				if ( this.value === currentTime) { // For Only time
						$("#exc_div_time_field").show();
						$("#exc_div_day_field").hide().val('');
						$("#exc_div_child_1_1").hide().val('');
						$("#exc_child_1_2").hide().val('');
						$("#exc_div_parent_3").hide().val('');
				}
				else if (this.value === currentDay){ //For only Day
						$("#exc_div_day_field").show();
						$("#exc_div_time_field").hide().val('');
						$("#exc_div_child_1_1").hide().val('');
						$("#exc_div_child_1_2").hide().val('');
						$("#exc_div_parent_3").hide().val('');

				}
				else {
						$("#exc_div_time_field").hide().val(''); // For MA_Cross, ST, BB, MACD
						$("#exc_div_day_field").hide().val('');
						$("#exc_div_child_1_1").show();
						$("#exc_div_child_1_2").show();
						$("#exc_div_parent_3").show();
				}
				if (this.value === 'pattern')   { // For Pattern
					$("#exc_div_child_1_2").hide().val('');
				}
		});
});



  $(document).ready(function(){
  		$("#trl_parent_1").on('change', function(abc) {
  			abc.preventDefault()
  				if ( this.value === currentTime) { // For Only time
  						$("#trl_div_time_field").show();
  						$("#trl_div_day_field").hide().val('');
  						$("#trl_div_child_1_1").hide().val('');
  						$("#trl_child_1_2").hide().val('');
  						$("#trl_div_parent_3").hide().val('');
							$("#trl_risk_value").hide().val('');
							$("#trl_profit").hide().val('');

  				}
  				else if (this.value === currentDay){ //For only Day
  						$("#trl_div_day_field").show();
  						$("#trl_div_time_field").hide().val('');
  						$("#trl_div_child_1_1").hide().val('');
  						$("#trl_div_child_1_2").hide().val('');
  						$("#trl_div_parent_3").hide().val('');
							$("#trl_risk_value").hide().val('');
							$("#trl_profit").hide().val('');

  				}
  				else {
  						$("#trl_div_time_field").hide().val(''); // For MA_Cross, ST, BB, MACD
  						$("#trl_div_day_field").hide().val('');
  						$("#trl_div_child_1_1").show();
  						$("#trl_div_child_1_2").show();
  						$("#trl_div_parent_3").show();
							$("#trl_risk_value").hide().val('');
							$("#trl+profit").hide().val('');

  				}
					if (this.value === 'pattern')   { // For Pattern
  					$("#trl_div_child_1_2").hide().val('');
  				}
					if (this.value === 'profit')   { // For Pattern
						$("#trl_div_time_field").hide().val('');
						$("#trl_div_day_field").hide().val('');
						$("#trl_div_child_1_1").hide().val('');
						$("#trl_child_1_2").hide().val('');
						$("#trl_div_parent_3").hide().val('');
						$("#trl_risk_value").hide().val('');
						$("#trl_profit").show();
					}
					if (this.value === 'risk_value')   { // For Pattern
						$("#trl_div_time_field").hide().val('');
						$("#trl_div_day_field").hide().val('');
						$("#trl_div_child_1_1").hide().val('');
						$("#trl_child_1_2").hide().val('');
						$("#trl_div_parent_3").hide().val('');
						$("#trl_risk_value").hide().val('');
						$("#trl_profit").hide().val('');
						$("#trl_risk_value").show();
					}
  		});
  });


	$(document).ready(function(){
			$("#rsk_child_1_1").on('change', function(abc) {
				abc.preventDefault()
					if (this.value === 'absolute')   { // For Pattern
						$("#rsk_abs_value").show().val('');
						$("#rsk_percentage").hide().val('');

					}
					else if (this.value === 'percentage')   { // For Pattern
						$("#rsk_percentage").show().val('');
						$("#rsk_abs_value").hide().val('');
					}
					else {
						$("#rsk_abs_value").hide().val('');
						$("#rsk_percentage").hide().val('');
					}
			});
	});

//  FOR ADD MORE BUTTON
// 	$(document).ready(function() {
//     var max_fields      = 10; //maximum input boxes allowed
//     var wrapper         = $(".entry_wrapper"); //Fields wrapper
//     var add_button      = $(".add_field_button"); //Add button ID
//
//     var x = 1; //initlal text box count
//
//
//    $(add_button).click(function(e){ //on add input button click
//         e.preventDefault();
//         if(x < max_fields){ //max input box allowed
// 					console.log(entryForm)
// 		     //text box increment
//             $(wrapper).append("entryForm"); //add input box
//             x++;
// 	  }
//     });
//
//     $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
//
// 		e.preventDefault();
// 		$(this).parent('div').remove();
// 		x--;
//     })
// });
