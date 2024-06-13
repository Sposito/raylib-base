#include <raylib.h>
#include <string.h>

int main(void) {
    int width = 800;
    int height = 480;


    InitWindow(width, height, "Base");

    const char* text = "Base: í ç ê à  $ . &";
    const int xPos = width/2 - strlen(text) * 48 / 4;



    while(!WindowShouldClose()) {

        BeginDrawing();
        ClearBackground(RAYWHITE);
        DrawCircle(width/2, height/2,height/4, YELLOW);
        DrawText(text, xPos, 240, 48, (Color){255,0,0,255ls});
        EndDrawing();
    }

    CloseWindow( );
    return 0;
}
