#include <raylib.h>
#include <stdio.h>
#include <string.h>



int main(void) {
    const int width = 800;
    const int height = 480;
#ifdef TESTING
    const double timeout = 5.0;
    printf("INFO: [TIMEOUT] = %f", timeout);
#endif

    InitWindow(width, height, "Base");

    const char* text = "Base: í ç ê à  $ . &";
    const int xPos = width/2 - strlen(text) * 48 / 4;

    while(!WindowShouldClose()) {

        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawCircle(width/2, height/2,height/4, YELLOW);
        DrawText(text, xPos, 240, 48, (Color){255,0,0,255});
        EndDrawing();
#ifdef TESTING
        if (GetTime() > timeout) {
            break;
        }
#endif

    }

    CloseWindow( );
    return 0;
}
