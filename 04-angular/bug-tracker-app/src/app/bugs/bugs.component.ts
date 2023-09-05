import { Component, OnInit } from "@angular/core";
import { Bug, NewBugOutput } from "./models/bug";
import { BugOperationService } from "./services/bugOperation.service";
import { BugsService } from "./services/bugs.service";
import { SortParams } from "./components/bug-sort/bug-sort.component";
import { ProjectsService } from "../projects/services/projects.service";
import { AuthService } from "./auth/auth.service";
import { HttpClient } from "@angular/common/http";

// using the bugs"Stateless" service
@Component({
    selector: 'app-bugs',
    templateUrl: 'bugs.component.html',
    styleUrls: ['bugs.component.css']
})
export class BugsComponent implements OnInit {

    sortAttr: string = '';
    sortDesc: boolean = false;

    showHeader: boolean = true;


    constructor(
        public bugsService: BugsService,
        public projectsService : ProjectsService,
        public httpClient : HttpClient,
        public authService : AuthService
    ) {
        console.log('bugsComponent - instance created')
    }

    // lifecycle method invoked when the component is initialized
    ngOnInit(): void {
        console.log('bugsComponent - initialized')
        this.bugsService.load()
        this.projectsService.load()
    }

    // event handler for the onNewBug event (bug-edit component)
    onNewBugCreate(newBug : NewBugOutput) {
        this.bugsService.addNew(newBug.title, newBug.projectId)
    }

    // event handler for the bug-sort component
    onSortChange(sortData: SortParams) {
        this.sortAttr = sortData.attrName;
        this.sortDesc = sortData.isDesc;
    }
}


/* 
@Component({
    selector: 'app-bugs',
    templateUrl: 'bugs.component.html',
    styleUrls: ['bugs.component.css']
})
export class BugsComponent implements OnInit {
    
    sortAttr : string = '';
    sortDesc : boolean = false;

    showHeader : boolean = true;
    

    constructor(public bugsService: BugsService) {
        console.log('bugsComponent - instance created')
    }

    // lifecycle method invoked when the component is initialized
    ngOnInit(): void {
        console.log('bugsComponent - initialized')
        this.bugsService.load()
    }

    // event handler for the onNewBug event (bug-edit component)
    onNewBugCreate(newBugTitle : string){
        this.bugsService.addNew(newBugTitle)
    }

    // event handler for the bug-sort component
    onSortChange(sortData : SortParams){
        this.sortAttr = sortData.attrName;
        this.sortDesc = sortData.isDesc;
    }

    getClosedCount(): number {
        console.log('getClosedCount triggered')
        return this.bugsService.bugs.reduce((prevResult, bug) => bug.isClosed ? prevResult + 1 : prevResult, 0)
    }
}
 */