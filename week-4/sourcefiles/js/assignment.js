/*
 * Author: Unekwu Shaibu
 * file name: form validation
 * Date: 26/08/2022
 */
			function check_reg()
			{
				name = document.getElementById('name').value
                        	firstpwd = document.getElementById('firstpwd').value
                        	secondpwd = document.getElementById('secondpwd').value
                        
                                if (((firstpwd === secondpwd) & (firstpwd != "" & secondpwd != "")) & (name != "" ))
                                         document.getElementById('success').innerHTML="<div class='alert alert-success'>Registration was successful</div>";
                                else
                                       	 alert('Validation error. Check your username or password');
					
                        }

