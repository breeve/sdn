//
// Created by 张锋 on 2019/12/28.
//

#ifndef __DEVICE_H__
#define __DEVICE_H__

#define DP_PORT_NAME (64)
#define DP_DEVICE_NAME (64)
#define DP_DEVICE_PORT_NUM (64)

typedef enum dp_device_type_ {
	ERROR_DEVICE_TYPE,
	SWITCH
} dp_device_type_t;

typedef struct dp_port_ {
	int port_id;
	char name[DP_PORT_NAME];
} dp_port_t;

typedef struct dp_device_ {
	int device_id;
    dp_device_type_t type;
	char name[DP_DEVICE_NAME];
	dp_port_t * port_list[DP_DEVICE_PORT_NUM];
} dp_device_t;

int device_init();

dp_device_t * device_create(dp_device_type_t type, char *name);

#endif
