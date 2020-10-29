// components/newsItem.js

Component({
    /**
     * 组件的属性列表
     */
    properties: {
        title:{
            value:"",
            type:String
        },
        like:{
            value: 0,
            type: Number,
        },
        comments:{
            value: 0,
            type: Number
        },
        time:{
            value: "",
            type: String
        },
        author:{
            value: "",
            type: String
        },
        imgUrl:{
            value: "",
            type: String
        },
        isTop:{
            value:false,
            type: Boolean
        }
    },

    /**
     * 组件的初始数据
     */
    data: {
        title:{
            default:"",
            type:String
        },
        like:{
            default: 0,
            type: Number,
        },
        comments:{
            default: 0,
            type: Number
        },
        time:{
            default: "",
            type: String
        },
        author:{
            default: "",
            type: String
        },
        imgUrl:{
            default: "",
            type: String
        },
        isTop:{
            default:false,
            type: Boolean
        }
    },

    /**
     * 组件的方法列表
     */
    methods: {

    }
})
