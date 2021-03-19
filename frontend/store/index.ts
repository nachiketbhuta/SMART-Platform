import { MutationTree } from 'vuex'

export const state = () => ({
    user: {},
    token: '',
    credential: {}
})

export type RootState = ReturnType<typeof state>

interface loginUserInfo{
    user: Object,
    token: string,
    credential: Object
}

export const mutations: MutationTree<RootState> = {
    loginUser(state, payload: loginUserInfo){
        state.user = payload.user
        state.token = payload.token
        state.credential = payload.credential
    }
}
