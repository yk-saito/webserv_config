# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ysaito <ysaito@student.42tokyo.jp>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/27 21:17:56 by ysaito            #+#    #+#              #
#    Updated: 2021/11/28 17:20:14 by ysaito           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM    debian:buster

RUN     apt-get update && apt-get -y upgrade \
        && apt-get -y install \
            nginx \
            vim

COPY    ./srcs/sites-available/webserv_default /etc/nginx/sites-available/webserv_default
COPY    ./srcs/html/ /html/

RUN     unlink /etc/nginx/sites-enabled/default \
        && ln -s /etc/nginx/sites-available/webserv_default /etc/nginx/sites-enabled/webserv_default

CMD     ["/usr/sbin/nginx", "-g", "daemon off;"]
