import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import UserCenter from "../views/user-center/index.vue";
const UserProfile = () => import("../views/user-center/Profile.vue");
const UserSettings = () => import("../views/user-center/Settings.vue");

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/user',
        name: 'UserCenter',
        component: UserCenter,
        redirect: '/user/profile',
        children: [
            {
                name: 'profile',
                path: 'profile',
                component: UserProfile
            },
            {
                name: 'settings',
                path: 'settings',
                component: UserSettings,
            }
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;