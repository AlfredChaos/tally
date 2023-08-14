<template>
    <div class="container">
        <div id="siderbar">
            <ul>
                <li>
                    <router-link to="/user/profile">个人信息</router-link>
                </li>
                <li>
                    <router-link to="/user/settings">用户设置</router-link>
                </li>
            </ul>
        </div>
        <div class="main-body">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
export default{
}
</script>

<style lang="css">
.container {
    display: flex;
    height: 100%;
    width: 100%;
}
#siderbar {
    width: 250px;
    height: 100%;
    background: #000;
}
#siderbar li {
    list-style: none;
}
#siderbar li a {
    display: block;
    height: 40px;
    line-height: 40px;
    text-decoration: none;
    color: #fff;
}
#siderbar li a.router-link-active {
    background: #f47c00;
}
.main-body {
    flex: 1;
    height: 100%;
    background: #f5f5f5;
}
</style>
