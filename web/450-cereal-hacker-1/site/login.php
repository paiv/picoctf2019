
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Sign In</h5>
														<form class="form-signin" action="index.php?file=login" method="post">
								<div class="form-label-group">
									<input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
									<label for="user">Username</label>
								</div>

								<div class="form-label-group">
									<input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
									<label for="pass">Password</label>
								</div>

								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>

	</body>
