<?php include 'assets/header_footer/header.php'; ?>



<main class="container register_main">
    <div class="row justify-content-center">
        <form class="registration" id="registr" method="POST">
        <div class="mb-3">
            <label for="name" class="form-label">Your Name</label>
            <input type="text" class="form-control" name="name" id="name" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="second_name" class="form-label">Second Name</label>
            <input type="text" class="form-control" name="second-name" id="second_name" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="email" class="form-label">Email address</label>
            <input type="email" class="form-control" name="email" id="email" aria-describedby="emailHelp">
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">Password</label>
            <input type="password" name="password" class="form-control" id="exampleInputPassword1">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    <div id="status"></div>
</main>




<?php include 'assets/header_footer/footer.php'; ?>