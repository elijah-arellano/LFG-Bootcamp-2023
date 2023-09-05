import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { BugsComponent } from "./bugs.component";
import { BugDetailsComponent } from "./components/bug-details/bug-details.component";
import { ReactiveFormsModule } from "@angular/forms";


const routes : Routes = [
    {
        path : "bugs", 
        component : BugsComponent,
        children : [ /* child routes for "bugs" route */
            { path: "details/:id", component: BugDetailsComponent } // :id => route parameter (data to be sent with the child route)
        ]
    }
]
@NgModule({
    imports : [
        RouterModule.forChild(routes)
    ],
    exports : [RouterModule]
})
export class BugsRoutingModule{

}